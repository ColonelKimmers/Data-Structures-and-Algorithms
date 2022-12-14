# Find 1st, find Nth...

CONST_ARRAY = ["hi", "my", "teddy"]
CONST_ARRAY[0] # O(1)
CONST_ARRAY[len(CONST_ARRAY)-1] # O(1)

CONST_ARRAY = """[{
    tweet: 'hi',
    date: 2012
    }, {
    tweet: 'my',
    date: 2014
    }, {
    tweet: 'teddy',
    date: 2018
    }
}]"""
# O(n^2)

len("helwoshejhekhiuhudsh") # Complexity depends on the language and how it implements length function
                            # Should be O(1)