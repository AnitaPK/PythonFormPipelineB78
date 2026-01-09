pipeline {
    agent any

    stages {
        stage 'Stage One get code' {
            steps {
                git branch : 'master' ,
                url: 'https://github.com/AnitaPK/PythonFormPipelineB78.git'
            }
        }
        stage 'stage Two check python' {
            steps {
                bat """ python --version """
            }
        }

        stage 'Stage Three installation' {
            steps {
                bat """ 
                    pip install -r requirements.txt
                """
            }
        }

        stage 'Stage four run project' {
            steps {
                bat """ 
                    python app.py
                """
            }
        }
    }
}