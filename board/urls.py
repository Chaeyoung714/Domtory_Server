from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    # 게시글 API
    path('post/create/<int:board_id>/', PostCreateView.as_view()), # 게시글 생성
    path('post/detail/<int:post_id>/', PostDetailView.as_view()), # 게시글 상세정보
    path('post/update/<int:post_id>/', PostUpdateView.as_view()), # 게시글 수정
    path('post/delete/<int:post_id>/', PostDeleteView.as_view()), # 게시글 삭제
    path('post/list/<int:board_id>/', PostListView.as_view()), # 특정 게시판의 게시글 리스트
    path('post/latest/<int:board_id>/', FreeBoardSimpleView.as_view()), # 특정 게시판의 최근 5개 게시글

    # 댓글 API
    path('comment/create/<int:post_id>/', CommentCreateView.as_view()), # 댓글 작성
    path('comment/delete/<int:comment_id>/', CommentDeleteView.as_view()), # 댓글 삭제
    path('reply/create/<int:comment_id>/', ReplyCreateView.as_view()), #대댓글 작성
    path('reply/delete/<int:reply_id>/', ReplyDeleteView.as_view()), # 대댓글 삭제
]