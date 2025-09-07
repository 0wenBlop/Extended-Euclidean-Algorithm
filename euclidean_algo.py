"""
Implementation of the (extended) Euclidean Algorithm
"""
import pandas as pd
import sys

class GCD:
    def __init__(self, a, b):
        a, b = abs(a), abs(b)
        a, b = max(a,b), min(a,b)

        if a == 0 and b == 0:
            raise ValueError("GCD undefined: (a,b)=({a},{b})")

        self.param = {
            "a": a,
            "b": b,
        }
        self.result = []
        self.gcd = self.euclidean_algo()

        self.linear_combination = [0, 0, 0, 0, 0]  # [gcd, s, a, t, b]

    def __str__(self):
        if len(self.result[-1]) != 2:
            print(pd.DataFrame(data=self.result, columns=["a", "b", "q", "r"]).to_string(index=None), end=f"\n\n")
        return f">> The GCD of {self.result[0][0]} and {self.result[0][1]} is: {self.gcd}"

    def euclidean_algo(self):
        while self.param["b"] != 0:
            self.param["q"] = self.param["a"]//self.param["b"]
            self.param["r"] = self.param["a"]%self.param["b"]
            
            self.result.append(tuple(self.param.values()))
            self.param["a"] = self.param["b"]
            self.param["b"] = self.param["r"]

        if not len(self.result):
            self.result.append((self.param["b"], self.param["a"]))

        return self.result[-1][1]

    def extended(self):
        print(">> ", end="")
        if len(self.result[0]) != 2:
            # In the form where they are perfect multiples
            if len(self.result) == 1:
                a, b, q, r = self.result[0]
                self.linear_combination[0] = r
                self.linear_combination[1] = 1
                self.linear_combination[2] = a
                self.linear_combination[3] = -q
                self.linear_combination[4] = b
            else:
                for step in range(len(self.result)-2, -1, -1):
                    a, b, q, r = self.result[step]

                    if step == len(self.result) - 2:
                        # Initialize linear combination
                        self.linear_combination[0] = r
                        self.linear_combination[1] = 1
                        self.linear_combination[2] = a
                        self.linear_combination[3] = -q
                        self.linear_combination[4] = b
                    else:
                        pos = 2 if self.linear_combination[2] == r else 4

                        self.linear_combination[5-pos] += (-q * self.linear_combination[pos-1])
                        self.linear_combination[pos] = a

                print(f"{self.linear_combination[0]} = {self.linear_combination[1]} x {self.linear_combination[2]} + {self.linear_combination[3]} x {self.linear_combination[4]}")
        else:
            print("By definition")


if __name__ == "__main__":
    try:
        gcd = GCD(int(sys.argv[1]), int(sys.argv[2]))
        print(gcd)
        gcd.extended()
    except IndexError as e:
        print("Error: Too little argument")
