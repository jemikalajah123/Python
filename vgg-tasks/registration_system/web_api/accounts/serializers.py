from rest_framework import serializers
from . models import Users,Projects,Actions

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        #fields = ('id','username','password')
        fields = '__all__'
        
    def save(self):
        user = Users(
            username =self.validated_data['username'],
            password =self.validated_data['password'],
        )
        user.save()
        return user

class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = '__all__'

    def save(self):
        user_project = Projects(
            name =self.validated_data['name'],
            description =self.validated_data['description'],
            completed =self.validated_data['completed'],
        )
        user_project.save()
        return user_project

class ActionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actions
        fields = '__all__'

    def save(self):
        user_action = Actions(
            project_id =self.validated_data['project_id'],
            description =self.validated_data['description'],
            note =self.validated_data['note'],
        )
        user_action.save()
        return user_action