from invoke import task


@task
def clean(ctx):
    clean_pyc(ctx)
    clean_test(ctx)


@task
def clean_pyc(ctx):
    patterns = ['**/*.pyc', '**/*.pyo', '**/__pycache__']
    for pattern in patterns:
        ctx.run('rm -rf %s' % pattern)


@task
def clean_test(ctx):
    patterns = ['.cache', '.coverage', 'htmlcov']
    for pattern in patterns:
        ctx.run('rm -rf %s' % pattern)


@task
def coverage(ctx, html=False):
    ctx.run('coverage erase')
    ctx.run('coverage run -m py.test')
    ctx.run('coverage report --show-missing')
    if html:
        ctx.run('coverage html')


@task
def lint(ctx):
    ctx.run('flake8 --show-source --count')


@task
def test(ctx):
    ctx.run('py.test', pty=True)
