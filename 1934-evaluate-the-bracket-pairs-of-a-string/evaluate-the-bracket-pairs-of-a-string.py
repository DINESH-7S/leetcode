class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        # Convert knowledge into a dictionary
        mp = {key: value for key, value in knowledge}

        result = []
        i = 0

        while i < len(s):

            if s[i] == '(':
                i += 1
                key = []

                # Read until ')'
                while s[i] != ')':
                    key.append(s[i])
                    i += 1

                key = ''.join(key)

                # Replace key
                result.append(mp.get(key, '?'))

                i += 1  # skip ')'

            else:
                result.append(s[i])
                i += 1

        return ''.join(result)