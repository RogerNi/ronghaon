# We know that the flag is 6x6 and evenly spaced in this 24x26 grid. The gap between each
# character can only be 3. However, the padding is unknown. We can extract all possible
# flags by iterating over all possible top-left starting points for the 6x6 grid. Then, we
# can select the one with correct English words.


def extract_all_possible_flags(grid, grid_size=(6, 6), gap=3):
    original_rows, original_cols = grid_size
    padded_rows = len(grid)
    padded_cols = len(grid[0]) if padded_rows > 0 else 0

    flags = []

    # Iterate over all possible top-left starting points for the 6x6 grid
    for top_padding in range(padded_rows - (original_rows + (original_rows - 1) * gap)):
        for left_padding in range(
            padded_cols - (original_cols + (original_cols - 1) * gap)
        ):
            hidden_text = []

            try:
                # Extract the flag for the current padding
                for i in range(original_rows):
                    row_index = top_padding + i * (gap + 1)
                    for j in range(original_cols):
                        col_index = left_padding + j * (gap + 1)
                        hidden_text.append(grid[row_index][col_index])

                flags.append("".join(hidden_text))
            except IndexError:
                continue

    return flags


padded_grid = """
paspipgrhkidojorbnogxmjqjh
eutjwjhphqixqasgnecubcremd
tfobphtftqbiivqzdeliinyxqj
gvbrpjfrmwzyvcmiolsbbkynxl
zjsgmvdnqdmgkhzzyijnpdsbck
gzyzyepeintymxokywsctqeafv
mnbvatyvqjtopfyyspkqxqjoim
tdhxotrqinmwsvcxlppgmdowfn
tszemrtstumffxxztiltqrggtv
hwewljmbdbsspunxzxonlbtpum
nvlsjdkhvojtywrfumkjzcuupa
bxysfizjdwycoymiedrvozubwn
fvzbiwxlmzspvmasnooteoiwik
ipspngaovpfalxeyelbznwurnv
hrwfrxoibvumtgoihqvkbzglei
izzrfhbobildrpafxpoqqoqmfq
podboyhbqlbisojsxrdfoyylkj
qrtwbxilpknssttdtpengvrcgm
igoeqlrwvuluewxrqavdbtixzf
mqldfytqvvvyuozycgkegygfgy
rtjyuzcnglpweyacrccwylhfwf
cpezfosvnitgmpisvvnkvfgpfi
euorftmewrqpvgnkawfknrcrrm
bskvxkogshyphorqotfpvmjbyg
"""

padded_grid = [list(row) for row in padded_grid.strip().split("\n")]
print(extract_all_possible_flags(padded_grid, grid_size=(6, 6), gap=3))

# The program should output:
# [
#     "pihobxzmqkyptmtftqfimvnepoqsxorugery",
#     "apkjnmjvdhidsruxirvwzmoooylorytzlycl",
#     "sgioojsdmzjsztmxlgzxsaoidhbjdyjcpach",
#     "prdrgqgngznbesfztgblpstwbbisflynwcwf",
#     "ihobxjmqkypcmtftqtimvneioqsxokugeryw",
#     "ewhqnbgyimythldpzlinvlenqbpstgcfnmvv",
#     "ujqaeczenxwqwjbuxbpgpxlwrxktpvpoipvf",
#     "thiscryptoseemsnotsafebutinteresting",
#     "jpxguezeykcawbsxnppoayzrwlsdnczvgskp",
#     "whqnbmyimytfldpzlunvlennbpstggfnmvvf",
#     "tptidimaqpsxnjvyuzhrbthbiqveqbefwvan",
#     "fhqvenntjfpqvdowmcrxvgqzgluwatutrgwr",
#     "otbqlybytykjlkjrkuwouovgorlxviomqnfc",
#     "bfizixvvoyqoshtfjufimiklewurdxrepkkr",
#     "ptidiqaqpsxijvyuzprbthbeqveqbzfwvanr",
# ]
# Only "thiscryptoseemsnotsafebutinteresting" is a good sentence.
# The flag is "thiscryptoseemsnotsafebutinteresting".
