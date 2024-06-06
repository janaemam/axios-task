from flask import request, jsonify, current_app as app
from .services import deposit, withdraw, get_balance, open_account, delete_account
from .schema import AccountSchema, TransactionSchema

@app.route('/create',methods=['POST'])
def create_account():
    name = request.json.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    account = open_account(name)
    account_schema = AccountSchema()
    return jsonify(account_schema.dump(account)), 201


@app.route('/deposit', methods=['POST'])
def make_deposit():
    id = request.json.get('id')
    amount = request.json.get('amount')

    if not id or not amount:
        return jsonify({'error': 'ID and amount are required'}), 400

    result, status = deposit(id, amount)
    if status != 200:
        return jsonify({'error': result}), status

    transaction_schema = TransactionSchema()
    return jsonify(transaction_schema.dump(result)), 200

@app.route('/withdraw', methods=['POST'])
def make_withdraw():
    id = request.json.get('id')
    amount = request.json.get('amount')

    if not id or not amount:
        return jsonify({'error': 'ID and amount are required'}), 400

    result, status = withdraw(id, amount)
    if status != 200:
        return jsonify({'error': result}), status

    transaction_schema = TransactionSchema()
    return jsonify(transaction_schema.dump(result)), 200


@app.route('/balance/<int:id>', methods=['GET'])
def balance(id):
    account = get_balance(id)
    if not account:
        return jsonify({'error': 'Account not found'}), 404

    return jsonify({'Owner': account.owner, 'Balance': account.balance}), 200


@app.route('/close/<int:id>', methods=['DELETE'])
def close_account(id):
    result, status = delete_account(id)
    if status!= 200:
        return jsonify({'error': result}), status
    
    return jsonify({'message': 'Account closed successfully'}), 200
