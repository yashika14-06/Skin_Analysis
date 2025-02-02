# def suggest_color(skin_tone):
#     suggestions = {
#         'Type I': 'Cool colors like blue, green',
#         'Type II': 'Soft pastels and light shades',
#         'Type III': 'Warm shades like peach, coral',
#         'Type IV': 'Earth tones like brown, olive',
#         'Type V': 'Bold colors like red, orange',
#         'Type VI': 'Bright shades and metallics'
#     }
#     return suggestions.get(skin_tone, 'Neutral tones')

def suggest_color(skin_tone):
    suggestions = {
        'Type I': 'Cool colors like sky blue, mint green, lavender, and icy pink. Avoid dark, overwhelming shades.',
        'Type II': 'Soft pastels and light shades such as peach, baby blue, soft yellow, and light lilac. Steer clear of deep, bold colors.',
        'Type III': 'Warm shades like coral, apricot, rich gold, and bronze. Earthy tones like olive green and burnt orange also complement well.',
        'Type IV': 'Earth tones like deep brown, forest green, mustard yellow, and terracotta. Jewel tones like emerald and sapphire enhance the skin glow.',
        'Type V': 'Bold colors like crimson red, royal blue, bright orange, and vivid purple. Metallics like gold and copper work wonderfully.',
        'Type VI': 'Bright shades and metallics such as electric blue, fuchsia, vibrant yellow, and shimmery silver. Deep jewel tones like ruby and amethyst add contrast.'
    }
    return suggestions.get(skin_tone, 'Neutral tones like beige, gray, and soft white work universally.')