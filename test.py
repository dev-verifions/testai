"""
semantic search prototype 
author: charlotte mcclintock

testing streamlit application implementation
"""
# %%
import streamlit as st


# use full width of page
st.set_page_config(layout="wide")


# define query to execute based on user submission # stripped out langchain/OpenAI calls for now
def process_query(query, n_results):

    return "Example summary", ['Quote 1', 'Quote 2', 'Quote 3']

# define Streamlit app
def main():
    # two columns layout
    col1, col2 = st.columns([3, 5], gap="large")

    # left column - user input widgets
    with col1:
        st.title("Public Remarks by State Officials")
        st.markdown(
            "*This semantic search application allows users to ask questions about public remarks and find policy insights.* "
        )

        # form submission box
        with st.form(key="qa_form"):
            # user prompt for policy topics
            query = st.text_area(
                "What have Department of State officials said about:",
                placeholder="AI, China, multilateralism, etc.",
            )

            # in dropdown box, let user select more criteria
            with st.expander("Advanced Options"):
                # select speaker
                options = st.multiselect(
                    "Speakers",
                    ["Secretary Blinken", "D-MR Verma"],
                    ["Secretary Blinken"],
                )

                # select number of results
                n_results = st.number_input(
                    "Max Results", min_value=1, max_value=100, value=10
                )

            # submit button
            submit = st.form_submit_button("Submit")

        st.divider()

        # dropdown with context: how does this work?
        with st.expander("How does this tool work?"):
            st.info(
                "This app is built using langchain, OpenAI, and Streamlit. All data is sourced from [Office of the Spokesperson](https://www.state.gov/press-releases/) via [state.gov](https://www.state.gov/). This v0 focuses only on S, but future extensions will include a range of speakers. "
            )
        # dropdown with context: accuracy
        with st.expander("How accurate is this search?"):
            st.info(
                "**Fuzzy search**: This app uses large language models to conduct *semantic* search (as opposed to lexical or keyword search) so information that is related to a term will be returned, even if it doesn't exactly match the term. This is helpful, particularly when you want to find anything related to a specific topic, but can occasionally return unrelated information, particularly for topics with few matches (e.g. search for 'Obama' returns other matches for 'Mr. President'). \n\n**The app will never make up quotes:** All quotes returned are verbatim quotes from public speeches."
            )

    # right column: results
    with col2:
        if submit:
            # execute query
            summary, result = process_query(query, n_results)

            # write summary
            st.markdown("## Summary")
            st.write(summary)

            # write quotes
            st.markdown("## Quotes")

            for doc in result:
                # return quote + write
                st.info(doc)

                st.divider()


if __name__ == "__main__":
    main()

# %%