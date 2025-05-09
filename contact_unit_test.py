import unittest
from app import app, db, Contact

class ContactModelTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        self.app = app.test_client()
        
        # Push application context
        self.app_context = app.app_context()
        self.app_context.push()
        
        db.create_all()

    def tearDown(self):
        # Clean up the test database
        db.session.remove()
        db.drop_all()
        
        # Pop application context
        self.app_context.pop()

    def test_contact_creation(self):
        # Create a new contact
        contact = Contact(name='Carlos Test', email='CarlosTest@example.com', message='Hello, this is a test message.')
        db.session.add(contact)
        db.session.commit()

        # Retrieve the contact from the database
        retrieved_contact = Contact.query.filter_by(name='Carlos Test').first()
        self.assertIsNotNone(retrieved_contact)
        self.assertEqual(retrieved_contact.email, 'CarlosTest@example.com')
        self.assertEqual(retrieved_contact.message, 'Hello, this is a test message.')

    def test_contact_repr(self):
        # Test the __repr__ method
        contact = Contact(name='Dog Cat', email='DogCat@example.com', message='Another test message.')
        self.assertEqual(repr(contact), '<Contact Dog Cat>')

if __name__ == '__main__':
    unittest.main()