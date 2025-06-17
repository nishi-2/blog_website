from flask import Blueprint, render_template

ml_bp = Blueprint('ml_bp', __name__, url_prefix='/ml')


@ml_bp.route('/')
def ml_page():
    return render_template('landing_page_directing_to_templates/ml_page.html')


@ml_bp.route('/ml_data_preprocessing')
def ml_preprocessing_page():
    return render_template('machine_learning_templates/machine_learning_blogs/machine_learning_data_preprocessing_main_page.html')


@ml_bp.route('/ml_regression')
def ml_regression_page():
    return render_template('machine_learning_templates/machine_learning_blogs/machine_learning_regression_main_page.html')


@ml_bp.route('/ml_classification')
def ml_classification_page():
    return render_template('machine_learning_templates/machine_learning_blogs/machine_learning_classification_main_page.html')




# Blog end points
@ml_bp.route('/ml_data_preprocessing/topic_one')
def topic_1():
    return render_template('machine_learning_templates/machine_learning_blogs/Blogs/Part_1_Intro.html')

@ml_bp.route('/ml_data_preprocessing/topic_two')
def topic_2():
    return render_template('machine_learning_templates/machine_learning_blogs/Blogs/Part_2_Process_Follow.html')

@ml_bp.route('/ml_data_preprocessing/topic_three')
def topic_3():
    return render_template('machine_learning_templates/machine_learning_blogs/Blogs/Part_3_ways_to_collect.html')

@ml_bp.route('/ml_data_preprocessing/topic_four')
def topic_4():
    return render_template('machine_learning_templates/machine_learning_blogs/Blogs/Part_4_data_preprocessing_intro.html')

@ml_bp.route('/ml_data_preprocessing/topic_five')
def topic_5():
    return render_template('machine_learning_templates/machine_learning_blogs/Blogs/Part_5_Handling_Missing_Values.html')

@ml_bp.route('/ml_data_preprocessing/topic_six')
def topic_6():
    return render_template('machine_learning_templates/machine_learning_blogs/Blogs/Part_6_Handling_Outliers.html')

@ml_bp.route('/ml_data_preprocessing/topic_seven')
def topic_7():
    return render_template('machine_learning_templates/machine_learning_blogs/Blogs/Part_7_Exploratory_Data_Analysis.html')

@ml_bp.route('/ml_data_preprocessing/topic_eight')
def topic_8():
    return render_template('machine_learning_templates/machine_learning_blogs/Blogs/Part_8_Basic_EDA_Project.html')





# Project End points
@ml_bp.route('/ml_regression/housing_project')
def regression_project_one():
    return render_template('machine_learning_templates/machine_learning_blogs/Projects/Regression/Housing_Project.html')


@ml_bp.route('/ml_classification/handwritten_digits_project')
def classification_project_one():
    return render_template('machine_learning_templates/machine_learning_blogs/Projects/Classification/Handwritten_Digit_Classification.html')


