from rest_framework import serializers
from api.models import *

class postSerializer1(serializers.ModelSerializer):
   class Meta:
      model = Exam1
      fields= ('ques','ans','option1', 'option2','option3', 'option4', 'time')




class postSerializer2(serializers.ModelSerializer):
   class Meta:
      model = Exam2
      fields= ('ques','ans','option1', 'option2','option3', 'option4', 'time')


class postSerializer3(serializers.ModelSerializer):
   class Meta:
      model = Exam3
      fields= ('ques','ans','option1', 'option2','option3', 'option4', 'time')


class postSerializer4(serializers.ModelSerializer):
   class Meta:
      model = Exam4
      fields= ('ques','ans','option1', 'option2','option3', 'option4', 'time')

class postSerializer5(serializers.ModelSerializer):
   class Meta:
      model = Exam5
      fields= ('ques','ans','option1', 'option2','option3', 'option4', 'time')

class postSerializer6(serializers.ModelSerializer):
   class Meta:
      model = General_science
      fields= ('ques',)


class postSerializer7(serializers.ModelSerializer):
   class Meta:
      model = Current_affairs
      fields= ('ques',)

class postSerializer8(serializers.ModelSerializer):
   class Meta:
      model = English
      fields= ('ques',)


