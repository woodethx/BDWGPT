from flask import Blueprint, render_template, redirect, url_for, request

from . import db
from .models import Order, System, ChecklistItem

main = Blueprint('main', __name__)


@main.route('/')
def index():
    orders = Order.query.all()
    statuses = ['Ordered', 'In progress', 'Ready to deliver', 'Complete']
    return render_template('index.html', orders=orders, statuses=statuses)


@main.route('/order/<int:order_id>')
def view_order(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order.html', order=order)


@main.route('/order/<int:order_id>/move', methods=['POST'])
def move_order(order_id):
    order = Order.query.get_or_404(order_id)
    status = request.form.get('status')
    order.status = status
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/system/<int:system_id>/check', methods=['POST'])
def check_item(system_id):
    item_id = request.form.get('item_id')
    item = ChecklistItem.query.get_or_404(item_id)
    if request.form.get('action') == 'complete':
        item.completed = not item.completed
    elif request.form.get('action') == 'qa':
        item.qa_checked = not item.qa_checked
    db.session.commit()
    return redirect(url_for('main.view_order', order_id=item.system.order_id))
