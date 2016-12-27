import unittest

from intsights.task.main import MyDaemon
from intsights.task.runner import Runner

class TestDaemon(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.runner = MockRunner()  
        self.mydaemon = MyDaemon(self.runner, 1)
        self.mydaemon.run()
    def test_run(self):
        #check if it does run
        pass
        
    def testName(self):
        return 'TestDaemon'
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    
class MockRunner(Runner):
    def __init__(self):
        pass
    def run(self):
        pass