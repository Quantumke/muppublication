from publication.models import news_posts
class GetCount():
    def run(daat, slug):
        slug=news_post.objects.filter(slug=slug)
        count=slug.get('count')
        print(slug)
        news_posts.objects.filter(slug=slug).update(count=count+1)
