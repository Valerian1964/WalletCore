# test_walletcore.py
"""
Tests for WalletCore module.
"""

import unittest
from walletcore import WalletCore

class TestWalletCore(unittest.TestCase):
    """Test cases for WalletCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletCore()
        self.assertIsInstance(instance, WalletCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
