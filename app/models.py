from datetime import datetime

from . import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(128))
    status = db.Column(db.String(64), default='Ordered')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    systems = db.relationship('System', backref='order', lazy=True)


class System(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    name = db.Column(db.String(128))
    serial_number = db.Column(db.String(128))
    checklist_items = db.relationship('ChecklistItem', backref='system', lazy=True)


class ChecklistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    system_id = db.Column(db.Integer, db.ForeignKey('system.id'))
    description = db.Column(db.String(256))
    completed = db.Column(db.Boolean, default=False)
    qa_checked = db.Column(db.Boolean, default=False)
