from flask import jsonify
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    """处理404错误"""
    return jsonify({
        'status': 'error',
        'message': '请求的资源不存在'
    }), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    """处理500错误"""
    return jsonify({
        'status': 'error',
        'message': '服务器内部错误'
    }), 500

@main.app_errorhandler(400)
def bad_request(e):
    """处理400错误"""
    return jsonify({
        'status': 'error',
        'message': '错误的请求'
    }), 400

@main.app_errorhandler(403)
def forbidden(e):
    """处理403错误"""
    return jsonify({
        'status': 'error',
        'message': '禁止访问'
    }), 403

@main.app_errorhandler(405)
def method_not_allowed(e):
    """处理405错误"""
    return jsonify({
        'status': 'error',
        'message': '不允许的请求方法'
    }), 405