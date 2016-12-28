import unittest
import procname

from intsights.task.main import MyDaemon
from intsights.task.runner import Runner

class TestDaemon(unittest.TestCase):
    @staticmethod
    def make_daemon_name():
        import uuid
        return 'MyDaemonTest' + str(uuid.uuid4()).replace('-','')[0:7]
    def setUp(self):
        unittest.TestCase.setUp(self)
        procname.setprocname(self.make_daemon_name())
        self.runner = MockRunner()  
        self.mydaemon = MyDaemon(self.runner, 1)
        self.mydaemon.run()
        
        
    def testUp(self):
        #look at the linux processes and find the daemon
        #what will be its name ?
        
        
    def test(self):
        #check if it does run
        print('what')
#         self.assertEqual(0, 1, "sdsa")
# 
#     def test2(self):
#         #check if it does run
#         print('what')
#     #         self.assertEqual(0, 1, "sdsa")
        
#     def testName(self):
#         return 'TestDaemon'
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    
class MockRunner(Runner):
    def __init__(self):
        pass
    def run(self):
        pass