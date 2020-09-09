import logging

from flask import abort, render_template, redirect, url_for, request, current_app, send_file, flash
from flask_login import current_user

from app.models import Post, Comment
from . import public_bp
from .forms import CommentForm, ContactForm

logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    logger.info('Displaying blog posts')
    page = int(request.args.get('page', 1))
    per_page = current_app.config['ITEMS_PER_PAGE']
    post_pagination = Post.all_paginated(page, per_page)
    return render_template("public/index.html", post_pagination=post_pagination)


@public_bp.route("/spiderweb")
def spiderweb():
    return render_template("spiderweb.html")


@public_bp.route("/patch")
def patch():
    logger.info('Displaying blog posts')
    posts = Post.get_all()
    return render_template("public/deployment.html", posts=posts)


@public_bp.route("/documentation")
def documentation():
    return render_template("documentation.html")


@public_bp.route('/about', methods=['GET', 'POST'])
def about():
    form = ContactForm()

    if request.method == 'POST':
        return 'Form posted.'

    elif request.method == 'GET':
        return render_template('public/contact.html', form=form)


@public_bp.route("/p/<string:slug>/", methods=['GET', 'POST'])
def show_post(slug):
    logger.info('Showing a post')
    logger.debug(f'Slug: {slug}')
    post = Post.get_by_slug(slug)
    if not post:
        logger.info(f'Post {slug} does not exist')
        abort(404)
    form = CommentForm()
    if current_user.is_authenticated and form.validate_on_submit():
        content = form.content.data
        comment = Comment(content=content, user_id=current_user.id,
                          user_name=current_user.name, post_id=post.id)
        comment.save()
        return redirect(url_for('public.show_post', slug=post.title_slug))
    return render_template("public/post_view.html", post=post, form=form)


@public_bp.route("/patch/p/<string:slug>/", methods=['GET', 'POST'])
def show_patch(slug):
    logger.info('Showing a post')
    logger.debug(f'Slug: {slug}')
    post = Post.get_by_slug(slug)
    if not post:
        logger.info(f'Post {slug} does not exist')
        abort(404)
    form = CommentForm()
    if current_user.is_authenticated and form.validate_on_submit():
        content = form.content.data
        comment = Comment(content=content, user_id=current_user.id,
                          user_name=current_user.name, post_id=post.id)
        comment.save()
        return redirect(url_for('public.show_patch', slug=post.title_slug))
    return render_template("public/patch_view.html", post=post, form=form)


@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)


@public_bp.route('/robots.txt')
def send_robots_txt():
    return send_file(current_app.config['BASE_DIR'] + '/robots.txt')


@public_bp.route('/sitemap.xml')
def send_sitemap_xml():
    return send_file(current_app.config['BASE_DIR'] + '/sitemap.xml')


@public_bp.route('/feed')
def send_feed_rss():
    return send_file(current_app.config['BASE_DIR'] + '/feed.rss')



