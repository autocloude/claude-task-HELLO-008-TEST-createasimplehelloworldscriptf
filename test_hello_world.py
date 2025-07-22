import pytest
from hello_world import hello_world


class TestHelloWorld:
    """Test suite for hello_world function."""
    
    def test_hello_world_returns_string(self):
        """Test that hello_world returns a string."""
        result = hello_world()
        assert isinstance(result, str)
    
    def test_hello_world_returns_correct_message(self):
        """Test that hello_world returns 'Hello World'."""
        result = hello_world()
        assert result == "Hello World"
    
    def test_hello_world_no_parameters_required(self):
        """Test that hello_world can be called without parameters."""
        # Should not raise any exception
        result = hello_world()
        assert result is not None
    
    def test_hello_world_consistent_output(self):
        """Test that hello_world returns consistent output across multiple calls."""
        result1 = hello_world()
        result2 = hello_world()
        assert result1 == result2
    
    def test_hello_world_not_empty(self):
        """Test that hello_world doesn't return empty string."""
        result = hello_world()
        assert result != ""
        assert len(result) > 0
    
    def test_hello_world_exact_case(self):
        """Test that hello_world returns exact case 'Hello World'."""
        result = hello_world()
        assert result == "Hello World"
        assert result != "hello world"
        assert result != "HELLO WORLD"
        assert result != "Hello world"