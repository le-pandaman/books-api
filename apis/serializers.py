from rest_framework import serializers

from books.models import Books


class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Books

        fields = ('title', 'subtitle', 'author', 'isbn')

    def validate_title(self, title):

        if title is None:
            raise serializers.ValidationError('Title must not be empty')

        return title
