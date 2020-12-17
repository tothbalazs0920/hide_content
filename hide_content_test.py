import unittest
import hide_content
from bs4 import BeautifulSoup


class HideContentTest(unittest.TestCase):

    def remove_images_from_html_removes_all_of_the_images(self):
        html= """<html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>
        <img src="img_chania.jpg" alt="Flowers in Chania">
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <img src="pic_trulli.jpg" alt="Italian Trulli">
        <img src="img_girl.jpg" alt="Girl in a jacket">
        <p class="story">...</p>
        </body>
        </html>
        """

        result = hide_content.remove_images_from_html(html)
        soup = BeautifulSoup(result)
        img_tags = soup.findAll('img')
        self.assertEqual(0, len(img_tags))
        p_tags = soup.findAll('p')
        self.assertEqual(3, len(img_tags))


if __name__ == '__main__':
    hc = HideContentTest()
    hc.remove_images_from_html_removes_all_of_the_images()
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(HideContentTest))
