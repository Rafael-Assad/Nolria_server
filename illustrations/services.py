from django.core.files.images import get_image_dimensions


class IllustrationService:
    @staticmethod
    def illustration_instance_preparetion(request):
        illustration_info = request.data

        illustration_file = request.FILES['illustration']

        illust_title= illustration_info['title']
        illust_description= illustration_info['description']

        complete_hash = f'#{illustration_info["hash"]}'

        illust_width, illust_height = get_image_dimensions(illustration_file)
        illust_rows, illust_cols = IllustrationService.illustration_proportion(illust_width, illust_height)

        new_illustration={'title': illust_title,
                          'description': illust_description,
                          'illustration': illustration_file,
                          'rows': illust_rows,
                          'cols': illust_cols,
                          'hash': complete_hash}

        if 'home_order' in illustration_info \
        and int(illustration_info['home_order']) > 0\
        and int(illustration_info['home_order']) < 9:
            new_illustration['home_order'] = illustration_info['home_order']

        return new_illustration

    @staticmethod
    def illustration_proportion(width, height):
        height_x_width = height / width
        rows = 1
        cols = 1
        
        if height_x_width > 1:
            rows = 4
            cols = 4
        elif height_x_width < 1:
            rows = 3
            cols = 6
        else:
            rows = 2
            cols = 2
        return [rows, cols]