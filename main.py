def note_upper(mus_sign):
    convert_dict = {"BB": "B", "B": None, None: "#", "#": "X"}
    return convert_dict[mus_sign]


def note_lower(mus_sign):
    convert_dict = {"X": "#", "#": None, None: "B", "B": "BB"}
    return convert_dict[mus_sign]


def gamma_converter(gamma, upper_li, lower_li):
    res = {}
    counter = -1
    for k, v in gamma.items():
        counter += 1
        if counter in upper_li:
            res[k] = note_upper(v)
            continue
        if counter in lower_li:
            res[k] = note_lower(v)
            continue
        else:
            res[k] = v

    return res


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
        if gamma_type == "major":
            chromatic_up = gamma_converter(self.gamma_up, [0, 1, 3, 4], [6])
            chromatic_down = gamma_converter(self.gamma_down, [4], [1, 2, 5, 6])
            self.gamma = [chromatic_up, chromatic_down]
        if gamma_type == "minor":
            chromatic_up = gamma_converter(self.gamma_up, [2, 3, 5, 6], [1])
            chromatic_down = gamma_converter(self.gamma_down, [1, 2, 4, 5], [6])
            self.gamma = [chromatic_up, chromatic_down]


def main():
    gamma = Gamma(
        {
            "la": None, "si": None, "do": None, "re": None,
            "mi": None, "fa": None, "sol": None, "la2": None
        }
    )
    gamma.to_chromatic("minor")
    print(gamma.get_gamma())


if __name__ == "__main__":
    main()
