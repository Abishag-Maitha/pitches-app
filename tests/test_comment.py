import unittest
from app.models import Comment,User
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_comment = Comment(id=12345,pitch_id=123,title='Comment for pitches',comment='This pitch is the best thing since sliced bread',posted="date",user_id = self.user_James )

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,12345)
        self.assertEquals(self.new_comment.pitch_id,123)
        self.assertEquals(self.new_comment.title,'Comment for pitches')
        self.assertEquals(self.new_comment.comment,'This pitch is the best thing since sliced bread')
        self.assertEquals(self.new_comment.posted,'date')
        self.assertEquals(self.new_comment.user_id,self.user_James)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)