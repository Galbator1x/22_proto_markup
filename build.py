from staticjinja import make_site


if __name__ == "__main__":
    site = make_site(outpath='static')
    site.render(use_reloader=True)

