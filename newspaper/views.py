from django.shortcuts import render

# Create your views here.
class HomeView(TemplateView):
    model = "Post"
    template_name = "newsportal/home.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(
        published_at__isnull=False, status = "active"
    ).order_by("-published_at")[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breaking_news"] = Post.objects.filter(
            is_breaking_news=True,
            published_at__isnull=False,
            status="active"
        ).order_by("-published_at")[:3]
        context["featured_post"] = (
            Post.objects.filter(published_at__isnull=False, status="active")
            .order_by("-published_at", "views_count")
            .first()
        )
        context["trending_news"] = Post.objects.filter(
            published_at__isnull=False,
            status="active"
        ).order_by("-published_at")[:4]

        one_week_ago = timezone.now() - timedelta(days=7)
        context["weekly_top_posts"] = Post.objects.filter(
            published_at__isnull=False, status="active", published_at__gte=one_week_ago
        ).order_by("-published_at", "-views_count")[:5]
        return context