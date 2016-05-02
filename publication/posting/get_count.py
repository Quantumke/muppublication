from publication.models import news_posts
class GetCount():
    def run(data, slug):
        slug=news_posts.objects.get(slug=slug)
        count=slug.count
        count=int(count)
        count=count + 1
        id= slug.id
        print (id)
        news_posts.objects.filter(id=id).update(count=count)
        data['slug']= slug.slug
