from flask import Blueprint, render_template

dl_bp = Blueprint('dl_bp', __name__, url_prefix='/dl')


@dl_bp.route('/')
def dl_page():
    return render_template('landing_page_directing_to_templates/dl_page.html')


@dl_bp.route('/dl_begineer')
def begineer_main_page():
    return render_template('deep_learning_templates/deep_learning_blogs/deep_learning_begineer_main_page.html')

@dl_bp.route('/dl_intermediate')
def intermediate_main_page():
    return render_template('deep_learning_templates/deep_learning_blogs/deep_learning_intermediate_main_page.html')

@dl_bp.route('/dl_projects')
def projects_main_page():
    return render_template('deep_learning_templates/deep_learning_blogs/deep_learning_projects_main_page.html')





# Blog end points
@dl_bp.route('/dl_begineer/topic_one')
def topic_1():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_1.html')

@dl_bp.route('/dl_begineer/topic_two')
def topic_2():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_2.html')

@dl_bp.route('/dl_begineer/topic_three')
def topic_3():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_3.html')

@dl_bp.route('/dl_begineer/topic_four')
def topic_4():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_4.html')

@dl_bp.route('/dl_begineer/topic_five')
def topic_5():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_5.html')

@dl_bp.route('/dl_begineer/topic_six')
def topic_6():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_6.html')

@dl_bp.route('/dl_begineer/topic_seven')
def topic_7():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_7.html')

@dl_bp.route('/dl_begineer/topic_eight')
def topic_8():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_8.html')

@dl_bp.route('/dl_begineer/topic_nine')
def topic_9():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_9.html')

@dl_bp.route('/dl_begineer/topic_ten')
def topic_10():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_10.html')

@dl_bp.route('/dl_begineer/topic_eleven')
def topic_11():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_11.html')

@dl_bp.route('/dl_begineer/topic_twelve')
def topic_12():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_PART_12.html')

@dl_bp.route('/dl_begineer/topic_thirteen')
def topic_13():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/2.Cats Vs Dogs Image Classification.html')

@dl_bp.route('/dl_intermediate/topic_fourteen')
def topic_14():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/3.Dogs Vs Cats Classification with Augmentation.html')

@dl_bp.route('/dl_intermediate/topic_fifteen')
def topic_15():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/4.Humans and Horses classification with Augmentation.html')

@dl_bp.route('/dl_intermediate/topic_sixteen')
def topic_16():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/5.Cats and Dogs Image Classification with Augmentation and Earlycallback.html')

@dl_bp.route('/dl_intermediate/topic_seventeen')
def topic_17():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/6. Transfer Learning using Inception Model with Augmentation.html')

@dl_bp.route('/dl_intermediate/topic_eigthteen')
def topic_18():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/7. Transfer Learning with Inception without augmentation.html')

@dl_bp.route('/dl_intermediate/topic_nineteen')
def topic_19():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/8. MultiClass Classification of Images_Rock Paper Scissor.html')

@dl_bp.route('/dl_intermediate/topic_twenty')
def topic_20():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/9. Multiclass Sign language classification.html')

@dl_bp.route('/dl_intermediate/topic_twenty_one')
def topic_21():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_NLP_PART_1.html')

@dl_bp.route('/dl_intermediate/topic_twenty_two')
def topic_22():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_NLP_PART_2.html')

@dl_bp.route('/dl_intermediate/topic_twenty_three')
def topic_23():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_NLP_PART_3.html')

@dl_bp.route('/dl_intermediate/topic_twenty_four')
def topic_24():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_NLP_PART_5.html')

@dl_bp.route('/dl_intermediate/topic_twenty_five')
def topic_25():
    return render_template('deep_learning_templates/deep_learning_blogs/blogs/DL_NLP_PART_6.html')





# Project End points
@dl_bp.route('/dl_projects/project_one')
def project_1():
    return render_template('deep_learning_templates/deep_learning_blogs/projects/Happy and Sad Face emoji classification.html')

@dl_bp.route('/dl_projects/project_two')
def project_2():
    return render_template('deep_learning_templates/deep_learning_blogs/projects/BBC_News_Multiclass_Classification.html')

@dl_bp.route('/dl_projects/project_three')
def project_3():
    return render_template('deep_learning_templates/deep_learning_blogs/projects/MultiClass classification using VGG19.html')
