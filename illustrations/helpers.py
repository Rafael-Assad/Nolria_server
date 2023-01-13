from django.core.files.images import get_image_dimensions

def illustration_instance_preparetion(request):
    illustration_info = request.data

    illustration_file = request.FILES['illustration']
    illust_width, illust_height = get_image_dimensions(illustration_file)

    illust_title= illustration_info['title']
    illust_description= illustration_info['description']
    illust_rows, illust_cols= illustration_proportion(illust_width, illust_height)
    
    complete_hash = f'#{illustration_info["hash"]}'
    
    new_illustration={'title': illust_title,
                      'description': illust_description,
                      'illustration': illustration_file,
                      'rows': illust_rows,
                      'cols': illust_cols,
                      'hash': complete_hash}
    
    if 'home_order' in illustration_info and int(illustration_info['home_order']) > 0:
        new_illustration['home_order'] = illustration_info['home_order']

    return new_illustration

def illustration_proportion(width, height):
    rows = 1
    cols = 1
    return [rows, cols]