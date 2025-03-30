class finder:

    def getData(self):
        return ["HelloAI", "AI", "AI model", "Nevo", "Nevo AI"]

    def find(self,topics):
        for topic in topics:
            if "AI" in str(topic):
                print(topic)