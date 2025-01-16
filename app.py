from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user, current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chave_Secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

CORS(app)

class user(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False, unique=True)
  password= db.Column(db.String(10), nullable=False)
  Cart = db.relationship('cart', backref = 'user', lazy = True)

class produtos(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  price = db.Column(db.Float, nullable=False) 
  description = db.Column(db.Text, nullable=True)

class cart(db.Model): 
 id = db.Column(db.Integer, primary_key=True) 
 user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) 
 produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
 

@app.route('/api/products/add', methods=["POST"])
@login_required 
def add_products():
  data = request.json
  if 'name' in data and 'price' in data: 
   cadastro = produtos(name= data["name"], price= data["price"], description= data.get("description", ""))
   db.session.add(cadastro)
   db.session.commit()
   return jsonify({"message": "Produto cadastrado com sucesso!"}), 200
  return jsonify({"message": "Cadastro Invalido"}), 400   

@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])  
@login_required 
def del_products(product_id):
  remove = produtos.query.get(product_id)
  if remove:
    db.session.delete(remove)
    db.session.commit()
    return jsonify({"message": "Produto Deletado com sucesso!"}), 200
  return jsonify({"message": "Produto Não achado"}), 400   
 
@app.route('/api/products/<int:product_id>', methods=["GET"]) 
def get_product(product_id): 
  product = produtos.query.get(product_id)
  if product:
    return jsonify( {
        "id": product.id,
        "name": product.name, 
        "price": product.price,
        "description": product.description
     
      }
 
    )
  return jsonify({"message": "Produto não encontrado"}), 404


@login_manager.user_loader
def loader(user_id):
  return user.query.get(int(user_id))



@app.route('/login', methods=["POST"])
def login():
  data = request.json
  usuario = user.query.filter_by(name=data.get("name")).first()
  
  if usuario and data.get("password") == usuario.password:
   login_user(usuario)
   return jsonify({"message": "Login realizado com sucesso!"})
  return jsonify({"message": "Usuario ou Senha invalido"}), 401 

@app.route('/logout', methods=['POST'])
@login_required
def logout():
  logout_user()
  return jsonify({"message": "Até a Proxima"}) 

@app.route('/api/products/update/<int:product_id>', methods=["PUT"]) 
@login_required 
def update_product(product_id):
  product = produtos.query.get(product_id)
  if not product:
     return jsonify({"message": "Produto não encontrado"}), 404
  data = request.json
  if 'name' in data: 
     product.name = data['name']
  if 'price' in data:
     product.price = data['price']
  if 'description' in data: 
     product.description = data['description']

  db.session.commit() 
  return jsonify({"message": "Produto atualizado com sucesso!"})

@app.route('/api/products', methods=["GET"]) 
def get_productsall():
  products = produtos.query.all()
  products_list = []
  for product in products:
   all_products = {
   "id": product.id,
   "name": product.name, 
   "price": product.price
    }
   products_list.append(all_products)
  return jsonify(products_list)

@app.route('/api/cart/add/<int:product_id>', methods= ['POST'])
@login_required
def add_cart(product_id):
   usuario = user.query.get(int(current_user.id))
   product = produtos.query.get(product_id) 
   if usuario and product: 
     cart_items = cart(user_id = usuario.id, produto_id = product.id)
     db.session.add(cart_items)
     db.session.commit()
     return jsonify({'message': 'Produto adicionado com sucesso'})
   return jsonify({'message': 'Produto não encontrado'}), 400

@app.route('/api/cart/remove/<int:product_id>', methods= ['DELETE'])
@login_required
def remove_items(product_id):
 carrinho = cart.query.filter_by(user_id= current_user.id, produto_id = product_id).first()
 if carrinho:
   db.session.delete(carrinho)
   db.session.commit()
   return jsonify({'message': 'Produto deletado com sucesso'})
 return jsonify({'message': 'Produto não achado'}), 400

 
@app.route('/api/cart', methods=['GET']) 
@login_required
def get_cart():
  User = user.query.get(int(current_user.id))
  cart_item = User.Cart 
  content = []
  for item in cart_item:
     product = produtos.query.get(item.produto_id)
     content.append({
      "id": item.id,
      "user_id": item.user_id,
     "product_id": item.produto_id,
     "product_name": product.name,
     "price": product.price
     })
  return jsonify(content)

@app.route('/api/cart/checkout', methods=['POST'])
@login_required
def checkout():
 User = user.query.get(int(current_user.id))
 cart_item = User.Cart 
 for items in cart_item:
   db.session.delete(items) 
 db.session.commit()
 return jsonify({"message": "Checkout realizado com sucesso!"})

  
   


@app.route('/')
def hello_World():
 return "Deu certo"
if __name__ == "__main__":
    app.run(debug=True)


