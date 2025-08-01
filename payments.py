import stripe
from flask import Blueprint, request, jsonify
import os

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    data = request.json
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': data['product_name'],
                    },
                    'unit_amount': int(float(data['price'].strip('$')) * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://yourdomain.com/success',
            cancel_url='https://yourdomain.com/cancel',
        )
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify(error=str(e)), 400
