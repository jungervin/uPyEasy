# Autogenerated file
def render(info, plugindata):
    yield """
<!- DO NOT CHANGE LINE ABOVE! -->
<TR>
   <TD>Input Type:
   <TD>
      <select name='inputtype'>
      <option value='normal'"""
    if plugindata['inputtype'] == 'normal':
        yield """selected"""
    yield """>Normal Switch</option>
      <option value='low'"""
    if plugindata['inputtype'] == 'low':
        yield """selected"""
    yield """>Push Button Active Low</option>
      <option value='high'"""
    if plugindata['inputtype'] == 'high':
        yield """selected"""
    yield """>Push Button Active High</option>
      </select>
"""
    yield str(plugindata['content'])
