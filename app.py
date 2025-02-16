# todo_api/app.py
from flask import Flask, jsonify, request

app = Flask(__name__)  # 创建Flask应用实例

todos = []  # 临时存储TODO列表（后续替换为数据库）

@app.route('/todos', methods=['GET'])
def get_todos():
    """获取所有TODO项（关键点：RESTful GET接口）"""
    return jsonify({'todos': todos}), 200  # 返回JSON和状态码

@app.route('/todos', methods=['POST'])
def add_todo():
    """添加TODO项（关键点：请求体解析）"""
    data = request.get_json()  # 获取POST的JSON数据
    if 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    todos.append({'title': data['title'], 'done': False})
    return jsonify({'message': 'Todo added'}), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """更新指定TODO项（关键点：参数校验与错误处理）"""
    if todo_id >= len(todos) or todo_id < 0:
        abort(404, description="Todo项不存在")  # 自动返回404状态码
    
    data = request.get_json()
    if 'title' not in data or 'done' not in data:
        abort(400, description="请求参数不完整")
    
    todos[todo_id] = {'title': data['title'], 'done': data['done']}
    return jsonify({'message': 'Todo更新成功'}), 200


if __name__ == '__main__':
    app.run(debug=True)  # 调试模式运行（生产环境需关闭！）
