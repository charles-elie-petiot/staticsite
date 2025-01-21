from markdown import markdown_to_hmtl_node
import unittest

class TestMarkdown(unittest.TestCase):
    def test_mark_to_html(self):
        md = """### Big *test* !!! 

Il nous faut des paragraphes **classiques**. On peut y mettre des ![image test](https://image.com) et des liens [lien](https://lien.com)

Il faut aussi un peu de `code`

```Voir un bloc complet de `code` ```

* il faut
* une liste
* non ordonnée

1. et une
2. autre liste
3. ordonnée"""
        self.assertEqual(markdown_to_hmtl_node(md).to_html(), '<div><h3> Big <i>test</i> !!!</h3><p>Il nous faut des paragraphes <b>classiques</b>. On peut y mettre des <img src="https://image.com" alt="image test"></img> et des liens <a href="https://lien.com">lien</a></p><p>Il faut aussi un peu de <code>code</code></p><pre><code>Voir un bloc complet de <code>code</code> </code></pre><ul><li>il faut</li><li>une liste</li><li>non ordonnée</li></ul><ol><li> et une</li><li> autre liste</li><li> ordonnée</li></ol></div>')



if __name__ == "__main__":
    unittest.main()

