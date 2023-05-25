import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.hbnb = HBNBCommand()

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("quit")
        self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("EOF")
        self.assertEqual(f.getvalue(), "")

    def test_all(self):
        """Test all command with all classes"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("all")
        self.assertNotEqual(f.getvalue(), "")

    def test_all_with_class(self):
        """Test all command with a specific class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("all BaseModel")
        self.assertNotEqual(f.getvalue(), "")

    def test_all_with_dot_class(self):
        """Test all command with dot class syntax"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("all .BaseModel")
        self.assertNotEqual(f.getvalue(), "")

    def test_show(self):
        """Test show command with instance """
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("show BaseModel 123-123-123")
        self.assertNotEqual(f.getvalue(), "")

    def test_show_dot_class(self):
        """Test show command with dot class syntax"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("show BaseModel.123-123-123")
        self.assertNotEqual(f.getvalue(), "")

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("create BaseModel")
        self.assertNotEqual(f.getvalue(), "")

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("destroy BaseModel 123-123-123")
        self.assertEqual(f.getvalue(), "")

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("count BaseModel")
        self.assertNotEqual(f.getvalue(), "")

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("update BaseModel 123-123-123 name 'John'")
        self.assertEqual(f.getvalue(), "")

if __name__ == "__main__":
    unittest.main()