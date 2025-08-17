#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()



from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

a1 = Author("Alice")
a2 = Author("Bob")

m1 = Magazine("TechWorld", "Technology")
m2 = Magazine("DailyLife", "Lifestyle")

a1.add_article(m1, "The Future of AI")
a1.add_article(m2, "Living Simple")
a2.add_article(m1, "Cloud Computing Basics")


