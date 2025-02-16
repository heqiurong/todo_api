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

if __name__ == '__main__':
    app.run(debug=True)  # 调试模式运行（生产环境需关闭！）
