def note_upper(mus_sign):
    return "#" if mus_sign is None else "X"


def note_lower(mus_sign):
    return "B" if mus_sign is None else "BB"


class Gamma:
    def __init__(self, gamma_up=None):
        self.gamma_up = gamma_up if gamma_up is not None \
            else {
                "do": None, "re": None, "mi": None, "fa": None,
                "sol": None, "la": None, "si": None, "do2": None,
            }  # - for example

        self.gamma_down = {
            list(self.gamma_up.keys())[i]: list(self.gamma_up.values())[i]
            for i in range(len(self.gamma_up))[::-1]
        }

        self.gamma = [self.gamma_up, self.gamma_down]

    def get_gamma(self):
        return self.gamma

    def to_chromatic(self, gamma_type):
        chromatic_up = {}
        chromatic_down = {}
        if gamma_type == "major":
            counter = -1
            for k, v in self.gamma_up.items():
                counter += 1
                if counter in [0, 1, 3, 4]:
                    chromatic_up[k] = note_upper(v)
                    continue
                if counter == 6:
                    chromatic_up[k] = note_lower(v)
                    continue
                else:
                    chromatic_up[k] = v
            self.gamma = [chromatic_up, chromatic_down]


def main():
    gamma = Gamma(
        {
            "re": None, "mi": None, "fa": "#", "sol": None,
            "la": None, "si": None, "do": "#", "re2": None,
        }
    )
    gamma.to_chromatic("major")
    print(gamma.get_gamma())


if __name__ == "__main__":
    main()
