# AI-Powered Job Recommender System with MCP

A AI-powered job recommendation system that is to analyze resume data and provide personalized job recommendations from LinkedIn and Naukri.com.

## 🚀 Features

- **Resume Analysis**: Upload PDF resumes and get AI-powered analysis
- **Skill Gap Analysis**: Identify missing skills and areas for improvement
- **Career Roadmap**: Get personalized career development suggestions
- **Job Recommendations**: Fetch relevant jobs from LinkedIn and Naukri.com
- **Interactive Web Interface**: User-friendly Streamlit-based UI

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Apify API token

## 🛠️ Installation

1. **Create Virtual Environment**

   ```env
   python -m venv venv-name

   .\venv-name\Scripts\Activate
   ```

2. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd <project>
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory and add:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ENDPOINT=your_openai_endpoint_here
   APIFY_API_TOKEN=your_apify_api_token_here
   ```

## 🎯 Usage

### Running the Streamlit Web App

```bash
streamlit run app.py
```

The web application will be available at `http://localhost:8501`

### Running the MCP Server

```bash
python mcp_server.py
```

For development and testing:

```bash
mcp dev mcp_server.py
```

## 🔧 Core Components

### 1. Resume Analysis (`src/helper.py`)

- **PDF Text Extraction**: Uses PyMuPDF to extract text from uploaded resumes
- **AI-Powered Analysis**: Leverages OpenAI GPT-4 for resume summarization
- **Skill Gap Analysis**: Identifies missing skills and certifications
- **Career Roadmap**: Provides personalized development suggestions

### 2. Job Fetching (`src/job_api.py`)

- **LinkedIn Jobs**: Fetches jobs using Apify's LinkedIn scraper
- **Naukri Jobs**: Retrieves job listings from Naukri.com
- **Customizable Parameters**: Supports location, keyword, and result count filters

### 3. MCP Server (`mcp_server.py`)

- **FastMCP Integration**: Provides REST API endpoints
- **Tool Functions**: Exposes job fetching capabilities as tools
- **Async Support**: Handles concurrent requests efficiently

### 4. Web Interface (`app.py`)

- **File Upload**: Supports PDF resume uploads
- **Real-time Processing**: Shows progress with spinners
- **Responsive Design**: Mobile-friendly interface
- **Results Display**: Formatted job listings with direct links

## 🔑 API Keys Setup

### OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key
5. Add to your `.env` file

### Apify API Token

1. Visit [Apify Console](https://console.apify.com/)
2. Create an account or sign in
3. Go to Settings > Integrations
4. Copy your API token
5. Add to your `.env` file

## 📊 Usage Examples

### Basic Resume Analysis

1. Run the Streamlit app
2. Upload a PDF resume
3. Wait for AI analysis to complete
4. Review summary, skill gaps, and roadmap
5. Click "Get Job Recommendations" for job listings

### MCP Server Integration

```python
from mcp.server.fastmcp import FastMCP

# Use the MCP server tools
linkedin_jobs = await fetchlinkedin("python developer")
naukri_jobs = await fetchnaukri("data scientist")
```

## 🎨 Customization

### Modifying AI Prompts

Edit the prompts in `app.py` to customize analysis:

- Resume summarization prompt
- Skill gap analysis prompt
- Career roadmap generation prompt

### Adding New Job Sources

Extend `src/job_api.py` to include additional job platforms:

```python
def fetch_new_platform_jobs(search_query, location="india", rows=60):
    # Implementation for new job platform
    pass
```

### UI Customization

Modify the Streamlit interface in `app.py`:

- Change color schemes
- Add new sections
- Modify layout structure

## 🔍 Troubleshooting

### Common Issues

1. **API Key Errors**

   - Ensure `.env` file is properly configured
   - Check API key validity and permissions

2. **Package Installation Issues**

   - Use virtual environment
   - Upgrade pip: `pip install --upgrade pip`
   - Install packages individually if needed

3. **PDF Processing Errors**

   - Ensure PDF is not password-protected
   - Check file size (keep under 10MB)
   - Try different PDF files

4. **Job Fetching Issues**
   - Verify Apify API token
   - Check internet connectivity
   - Ensure sufficient API credits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for GPT-4 API
- Apify for job scraping capabilities
- Streamlit for the web interface framework
- PyMuPDF for PDF processing
- MCP community for protocol specifications

---

**Note**: This project is for educational and personal use. Ensure compliance with job platform terms of service when scraping data.
