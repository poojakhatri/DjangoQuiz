from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ques(models.Model): # Collection name
	# Documents
	_id = models.CharField(max_length=100, primary_key=True)
	si_no = models.IntegerField(null=True)
	level = models.IntegerField(null=True)
	question = models.TextField()
	ch_1 = models.TextField()
	ch_2 = models.TextField()
	ch_3 = models.TextField()	
	ch_4 = models.TextField()
	answer = models.CharField(max_length=10,null=True)


	class Meta:
		abstract = True

	def __str__(self):
		return str(self.level)

	@property
	def detail(self):
		return {
			"_id": self._id,
			"si_no": self.si_no,
			"level": self.level,
			"question":self.question,
			"ch_1": self.ch_1,
			"ch_2": self.ch_2,
			"ch_3": self.ch_3,
			"ch_4": self.ch_4,
			"answer": self.answer

		}
	
	@detail.setter
	def detail(self, any_):
		raise AttributeError
	
	

class Math(Ques):
	pass


class Stat(Ques):
	pass

	
class MathQuizAnswer(models.Model):
	user = models.ForeignKey(User, related_name="MathQuizAnswersAsUser", on_delete=models.CASCADE)
	mat_quiz = models.ForeignKey(Math, related_name="MathQuizAnswersAsMath", on_delete=models.CASCADE)
	CH_1 = "ch_1"
	CH_2 = "ch_2"
	CH_3 = "ch_3"
	CH_4 = "ch_4"
	CHOICES = (
		(CH_1, "Answer 1"),
		(CH_2, "Answer 2"),
		(CH_3, "Answer 3"),
		(CH_4, "Answer 4"),
	)
	answer = models.CharField(max_length=6, default='')


class StatQuizAnswer(models.Model):
	user = models.ForeignKey(User, related_name="StatQuizAnswersAsUser",on_delete=models.CASCADE)
	stat_quiz = models.ForeignKey('Stat', related_name="StatQuizAnswersAsStat",on_delete=models.CASCADE)
	CH_1 = "ch_1"
	CH_2 = "ch_2"
	CH_3 = "ch_3"
	CH_4 = "ch_4"
	CHOICES = (
		(CH_1, "Answer 1"),
		(CH_2, "Answer 2"),
		(CH_3, "Answer 3"),
		(CH_4, "Answer 4"),
	)
	answer = models.CharField(max_length=6, default='')