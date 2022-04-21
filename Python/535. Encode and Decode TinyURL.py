class Codec:
    def __init__(self):
        self.count = 0
        self.url_d = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        for (key, value) in self.url_d.items():
            if longUrl == value:
                return key
        self.count += 1
        shortUrl = "https://leetcode.com/shortUrl/" + str(self.count)
        self.url_d[shortUrl] = longUrl
        return shortUrl
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in self.url_d:
            return self.url_d[shortUrl]
        else:
            return 'error'
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))