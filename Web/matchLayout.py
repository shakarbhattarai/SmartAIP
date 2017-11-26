import dash as ds
import dash_html_components as html
import json
import pandas as pd
from pandas.io.json import json_normalize
import flask
import os


def generate_table(dataframe, classname='success', max_rows=100):
    if len(dataframe.index) <= 0:
        return html.Div(["No changes found."], className='alert alert-info')
    else:
        return html.Table(
            [html.Thead(
                # Header
                [html.Tr([html.Th([col], className='col-sm-2 success table-head-merge') for col in dataframe.columns])],
                className='text-primary')] +
            [html.Tbody(
                # Body
                [html.Tr([
                    html.Td([dataframe.iloc[i][col]], className='col-sm-2  table-row-merge') for col in
                    dataframe.columns
                ], className=classname) for i in range(min(len(dataframe), max_rows))])],
            className='table table-responsive table-bordered table-striped table-hover'
        )

def matchLayout(similarity):


    similarity=str(similarity*100)[:5]+'%'
    with open('output.json') as json_data:
        result = json.load(json_data)

#    similarity = result['similarity'][0]['similarity']
    reAdded = pd.DataFrame(json_normalize(result['added']), columns=["COLUMNNAME", "DATATYPE", "LAYOUTID"])
    reAdded.sort_values(['COLUMNNAME'],inplace=True)
    #reChanged = pd.DataFrame(json_normalize(result['changed']), columns=[ "field", "DATATYPE", "LAYOUTID"])
   # reChanged.sort_values(['COLUMNNAME'],inplace=True)
    reRemoved = pd.DataFrame(json_normalize(result['removed']), columns=["COLUMNNAME", "DATATYPE","LAYOUTID" ])
    reRemoved.sort_values(['COLUMNNAME'],inplace=True)

    finalColumns= (reAdded.join(reRemoved,lsuffix='_ADDED',rsuffix='_REMOVED'))



    application = ds.Dash()

    application.layout = html.Div([
        html.H4('Added and Removed Fields In Layout', className='text-primary'),
        html.P([html.P("Similarity Between the Layouts equals: "+similarity, style= {'color': '#083844','font-weight':'bold'})], className = 'alert alert-info  col-md-4', style ={'border-color':'#a2bf9f','background': 'linear-gradient(to bottom right, rgb(192, 239, 169), rgb(4, 140, 32) '+similarity+')'}),
        generate_table(finalColumns, classname='active'),
        #html.H4(children='Changed Field Names',  className='text-primary'),
        #generate_table(reChanged, classname='warning'),
        html.Footer([html.P('© él 7th Sense: Shakar Sabal Sujan Sheprata Kushma')], className = 'float-lg-right')
    ],className='container')

    css_directory = os.getcwd()
    stylesheets = ['custom.css']
    static_css_route = '/static/'


    @application.server.route('{}<stylesheet>'.format(static_css_route))
    def serve_stylesheet(stylesheet):
        if stylesheet not in stylesheets:
            raise Exception(
                '"{}" is excluded from the allowed static files'.format(
                    stylesheet
                )
            )
        return flask.send_from_directory(css_directory, stylesheet)


    for stylesheet in stylesheets:
        application.css.append_css({"external_url": "/static/{}".format(stylesheet)})

    application.css.append_css({
        # "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css",
         "external_url":"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
     })
    #app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"})
    application.run_server(debug=False)
