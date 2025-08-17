class Author:
    def __init__(self, name: str):
        if not isinstance(name, str) or len(name.strip()) == 0:
            return 
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        return 


    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        mags = list({article.magazine for article in self.articles()})
        return mags if mags else None

    def topic_areas(self):
        cats = list({article.magazine.category for article in self.articles()})
        return cats if cats else None

class Magazine:
    all_magazines = []

    def __init__(self, name: str, category: str):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            self._name = "AD"
        if isinstance(category, str) and len(category.strip()) > 0:
            self._category = category
        else:
            self._category = "Fashion"
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category.strip()) > 0:
            self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = list({article.author for article in self.articles()})
        return authors if authors else None

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        frequent = [a for a in set(authors) if authors.count(a) > 2]
        return frequent if frequent else None

    @classmethod
    def top_publisher(cls):
        mags_with_articles = [mag for mag in cls.all_magazines if mag.articles()]
        if not mags_with_articles:
            return None
        return max(mags_with_articles, key=lambda mag: len(mag.articles()))

class Article:
    all = []

    def __init__(self, author, magazine, title: str):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            return
        if not isinstance(author, Author):
            return
        if not isinstance(magazine, Magazine):
            return
        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine