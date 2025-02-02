# def determine_body_type(dimensions):
#     bust = dimensions.get('bust')
#     waist = dimensions.get('waist')
#     hips = dimensions.get('hips')

#     if bust and waist and hips:
#         if bust == hips and waist < bust:
#             return 'Hourglass'
#         elif hips > bust and waist < bust:
#             return 'Pear'
#         elif bust > hips and waist < hips:
#             return 'Apple'
#         else:
#             return 'Rectangle'
#     return 'Unknown'

def determine_body_type(dimensions):
    bust = dimensions.get('bust')
    waist = dimensions.get('waist')
    hips = dimensions.get('hips')

    if bust and waist and hips:
        if bust == hips and waist < bust:
            return 'Hourglass'
        elif hips > bust and waist < bust:
            return 'Pear'
        elif bust > hips and waist < hips:
            return 'Apple'
        else:
            return 'Rectangle'
    return 'Unknown'

def suggest_outfits(body_type):
    outfits = {
        'Hourglass': {
            'Jeans': 'High-waisted skinny jeans, bootcut jeans',
            'Dresses': 'Wrap dresses, bodycon dresses',
            'Tops': 'Fitted tops, V-neck blouses',
            'Shirts': 'Tailored button-down shirts'
        },
        'Pear': {
            'Jeans': 'Straight-leg jeans, flared jeans',
            'Dresses': 'A-line dresses, fit-and-flare dresses',
            'Tops': 'Off-shoulder tops, embellished necklines',
            'Shirts': 'Structured shirts with shoulder details'
        },
        'Apple': {
            'Jeans': 'Mid-rise bootcut jeans, straight-leg jeans',
            'Dresses': 'Empire waist dresses, shift dresses',
            'Tops': 'Flowy tops, tunics',
            'Shirts': 'Loose-fit button-down shirts'
        },
        'Rectangle': {
            'Jeans': 'Skinny jeans, boyfriend jeans',
            'Dresses': 'Sheath dresses, ruffle dresses',
            'Tops': 'Peplum tops, layered tops',
            'Shirts': 'Shirts with ruffles or pleats'
        },
        'Unknown': {
            'Jeans': 'Classic straight-leg jeans',
            'Dresses': 'Simple A-line dresses',
            'Tops': 'Basic fitted tees',
            'Shirts': 'Standard button-down shirts'
        }
    }
    return outfits.get(body_type, outfits['Unknown'])