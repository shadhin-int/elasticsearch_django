from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from elasticsearch_django.elasticsearch_in_django.blog.models import Post
#
#
# @registry.register_document
# class PostDocument(Document):
# 	class Index:
# 		name = 'posts'
# 		settings = {
# 			'number_of_shards': 1,
# 			'number_of_replicas': 0
# 		}
#
# 	class Django:
# 		model = Post
#
# 		fields = [
# 			'id', 'title', 'description', 'body', 'order', 'slug', 'image'
# 		]
