from textnode import TextNode, TextType

def main():
    text = "This is a text node"
    url = "https://www.boot.dev"
    node = TextNode(text, TextType.BOLD, url)
    print(node)

if __name__ == "__main__":
    main()
