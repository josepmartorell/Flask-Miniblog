import logging
import os

from flask import render_template, redirect, url_for, abort, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app.auth.decorators import admin_required
from app.auth.models import User
from app.models import Post
from . import admin_bp
from .forms import PostForm, UserAdminForm

logger = logging.getLogger(__name__)


@admin_bp.route("/admin/")
@login_required
@admin_required
def index():
    return render_template("admin/index.html")


@admin_bp.route("/admin/posts/")
@login_required
@admin_required
def list_posts():
    posts = Post.get_all()
    return render_template("admin/posts.html", posts=posts)


@admin_bp.route("/admin/post/", methods=['GET', 'POST'])
@login_required
@admin_required
def post_form():
    """Create a new post"""
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        file = form.post_image.data
        image_name = None
        # Check if a file has been uploaded
        if file:
            image_name = secure_filename(file.filename)
            images_dir = current_app.config['POSTS_IMAGES_DIR']
            os.makedirs(images_dir, exist_ok=True)
            file_path = os.path.join(images_dir, image_name)
            file.save(file_path)
        post = Post(user_id=current_user.id, title=title, content=content)
        post.image_name = image_name
        post.save()
        logger.info(f'Saving new post {title}')
        return redirect(url_for('admin.list_posts'))
    return render_template("admin/post_form.html", form=form)


@admin_bp.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_post_form(post_id):
    """Update an existing post"""
    post = Post.get_by_id(post_id)
    if post is None:
        logger.info(f'Post {post_id} does not exist')
        abort(404)
    # Create a form by initializing the fields with
    # the values of the post.
    form = PostForm(obj=post)
    if form.validate_on_submit():
        # Update the existing post fields
        post.title = form.title.data
        post.content = form.content.data
        file = form.post_image.data
        # Check if a file has been uploaded
        if file:
            image_name = secure_filename(file.filename)
            images_dir = current_app.config['POSTS_IMAGES_DIR']
            os.makedirs(images_dir, exist_ok=True)
            file_path = os.path.join(images_dir, image_name)
            file.save(file_path)
            post.image_name = image_name
        post.save()
        logger.info(f'Saving the post {post_id}')
        return redirect(url_for('admin.list_posts'))
    return render_template("admin/post_form.html", form=form, post=post)


@admin_bp.route("/admin/post/delete/<int:post_id>/", methods=['POST', ])
@login_required
@admin_required
def delete_post(post_id):
    logger.info(f'The post will be deleted {post_id}')
    post = Post.get_by_id(post_id)
    if post is None:
        logger.info(f'Post {post_id} does not exist')
        abort(404)
    post.delete()
    logger.info(f'Post {post_id} has been removed')
    return redirect(url_for('admin.list_posts'))


@admin_bp.route("/admin/users/")
@login_required
@admin_required
def list_users():
    users = User.get_all()
    return render_template("admin/users.html", users=users)


@admin_bp.route("/admin/user/<int:user_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_user_form(user_id):
    # Enter here to update an existing user
    user = User.get_by_id(user_id)
    if user is None:
        logger.info(f'User {user_id} does not exist')
        abort(404)
    # Create a form by initializing the fields with
    # the user values.
    form = UserAdminForm(obj=user)
    if form.validate_on_submit():
        # Update existing user fields
        user.is_admin = form.is_admin.data
        user.save()
        logger.info(f'Saving the user {user_id}')
        return redirect(url_for('admin.list_users'))
    return render_template("admin/user_form.html", form=form, user=user)


@admin_bp.route("/admin/user/delete/<int:user_id>/", methods=['POST', ])
@login_required
@admin_required
def delete_user(user_id):
    logger.info(f'User is going to be deleted {user_id}')
    user = User.get_by_id(user_id)
    if user is None:
        logger.info(f'User {user_id} does not exist')
        abort(404)
    user.delete()
    logger.info(f'User {user_id} has been removed')
    return redirect(url_for('admin.list_users'))
