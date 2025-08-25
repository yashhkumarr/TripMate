# Tripmate

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/Streamlit-1.48+-red?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Portia%20AI-0.7.2-purple?style=for-the-badge" alt="Portia AI">
  <img src="https://img.shields.io/badge/Google%20Gemini-1.5+-green?style=for-the-badge&logo=google&logoColor=white" alt="Google Gemini">
</div>

<div align="center">
  <h3>🚀 AI-Powered Travel Planning & Itinerary Generation</h3>
  <p>Transform your travel dreams into detailed, personalized itineraries with the power of artificial intelligence</p>
</div>

---

## 🌟 Overview

Tripmate is a sophisticated AI-driven travel planning application that revolutionizes how travelers plan their journeys. By leveraging cutting-edge AI technologies including Portia AI, Google Gemini, and advanced search capabilities, Tripmate creates comprehensive, personalized travel experiences tailored to individual preferences, budgets, and interests.

### Key Capabilities
- **Intelligent Itinerary Generation**: AI-powered creation of detailed day-by-day travel plans
- **Real-time Recommendations**: Dynamic suggestions based on current trends and local insights
- **Automated Communication**: Seamless email delivery and calendar integration
- **Personalized Experiences**: Customization based on travel style, budget, and preferences

---

## 📁 Project Structure

### File Descriptions
| File | Purpose |
|------|---------|
| **`app.py`** | Main Streamlit application with AI-powered travel planning interface |
| **`requirements.txt`** | Python dependencies and package specifications |
| **`.env`** | Environment variables and API key configuration |
| **`README.md`** | Project documentation and setup instructions |
| **`test_portia.py`** | Test suite for Portia AI integration functionality |
| **`test.py`** | Basic application testing and validation scripts |

---

## 🛠️ Technology Architecture

### Core Technologies
| Component | Technology | Version |
|-----------|------------|---------|
| **Frontend Framework** | Streamlit | 1.48+ |
| **AI Orchestration** | Portia AI | 0.7.2 |
| **Language Model** | Google Gemini | 1.5+ |
| **Search Engine** | Tavily API | Latest |
| **Development Language** | Python | 3.11+ |

### AI Integration Stack
- **Portia AI**: Advanced agent orchestration and workflow management
- **Google Gemini**: Natural language processing and intelligent reasoning
- **Tavily Search**: Real-time web search for up-to-date travel information
- **Browser Automation**: Dynamic content gathering and analysis

---

## ✨ Features

### 🎯 Smart Planning Engine
- **Destination Intelligence**: AI-powered analysis of destinations, attractions, and local insights
- **Budget Optimization**: Intelligent recommendations based on specified budget constraints
- **Seasonal Awareness**: Consideration of weather, events, and seasonal factors
- **Accessibility Features**: Recommendations considering mobility and accessibility needs

### 📧 Automated Communication System
- **Comprehensive Reports**: Detailed itineraries with maps, recommendations, and tips
- **Email Automation**: Instant delivery of travel plans to multiple recipients
- **Calendar Integration**: Automatic scheduling of travel events and reminders
- **Multi-format Output**: Support for various export formats and sharing options

### 🔍 Advanced Search & Discovery
- **Real-time Information**: Live data from multiple sources for current recommendations
- **Local Expertise**: Insights from local sources and recent traveler experiences
- **Trend Analysis**: Identification of emerging destinations and experiences
- **Custom Research**: Tailored information gathering based on specific interests

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- Valid API keys for required services
- Modern web browser for optimal experience

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yashhkumarr/tripmate.git
   cd tripmate
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the project root:
   ```bash
   PORTIA_API_KEY=your_portia_api_key_here
   GEMINI_API_KEY=your_google_gemini_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

5. **Launch the Application**
   ```bash
   streamlit run app.py
   ```

### API Key Setup

#### Portia AI
1. Visit [Portia Labs](https://www.portialabs.ai/)
2. Create an account and generate your API key
3. Add to your `.env` file as `PORTIA_API_KEY`

#### Google Gemini
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key for Gemini
3. Add to your `.env` file as `GEMINI_API_KEY`

#### Tavily Search
1. Visit [Tavily](https://www.tavily.com/)
2. Sign up and obtain your API key
3. Add to your `.env` file as `TAVILY_API_KEY`

---

## 📱 User Interface

### Modern Design Philosophy
- **Clean, Professional Layout**: Minimalist design focusing on user experience
- **Responsive Design**: Optimized for various screen sizes and devices
- **Intuitive Navigation**: Logical flow from planning to execution
- **Visual Feedback**: Clear status indicators and progress tracking

### Key Interface Elements
- **Trip Planning Form**: Comprehensive input fields for all travel details
- **Real-time Validation**: Instant feedback on form completion and requirements
- **Progress Tracking**: Visual indicators for AI processing stages
- **Results Display**: Organized presentation of generated itineraries

---

## 🔄 Workflow Process

### 1. Information Input
Users provide comprehensive travel details including:
- Origin and destination locations
- Travel dates and duration
- Budget constraints and preferences
- Activity interests and special requirements
- Contact information for report delivery

### 2. AI Analysis & Planning
The system processes inputs through multiple AI layers:
- **Portia AI**: Orchestrates the overall planning workflow
- **Gemini AI**: Analyzes requirements and generates intelligent suggestions
- **Tavily Search**: Gathers current information about destinations and activities

### 3. Itinerary Generation
AI creates detailed travel plans including:
- Day-by-day activity schedules
- Transportation recommendations
- Accommodation suggestions
- Dining and entertainment options
- Local insights and tips

### 4. Delivery & Integration
Automated delivery systems:
- Email reports with comprehensive details
- Calendar event creation and invitations
- Export options for various formats
- Integration with travel management tools

---

## 🧪 Testing & Development

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest test_portia.py

# Run with coverage
python -m pytest --cov=app
```

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Set up pre-commit hooks
pre-commit install

# Run linting
flake8 app.py
black app.py
```

---

## 📊 Performance & Scalability

### Optimization Features
- **Caching System**: Intelligent caching of AI responses and search results
- **Async Processing**: Non-blocking operations for better user experience
- **Resource Management**: Efficient memory and API usage optimization
- **Error Handling**: Robust error management and recovery systems

### Scalability Considerations
- **Modular Architecture**: Easy to extend with new features and integrations
- **API Rate Limiting**: Intelligent management of external API calls
- **Load Balancing**: Support for multiple concurrent users
- **Database Integration**: Ready for persistent storage and user management

---

## 🤝 Contributing

We welcome contributions to make Tripmate even better! Here's how you can help:

### Contribution Guidelines
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** with clear, documented code
4. **Test thoroughly** to ensure no regressions
5. **Submit a pull request** with detailed description

### Development Standards
- Follow PEP 8 Python style guidelines
- Write comprehensive tests for new features
- Update documentation for any API changes
- Ensure all tests pass before submitting

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**MIT License Benefits:**
- ✅ Free to use for commercial and personal projects
- ✅ Permission to modify and distribute
- ✅ Minimal restrictions and requirements
- ✅ Compatible with most other licenses

---

## 🆘 Support & Community

### Getting Help
- **Documentation**: Comprehensive guides and API references
- **Issues**: Report bugs and request features via GitHub Issues
- **Discussions**: Join community conversations on GitHub Discussions
- **Wiki**: Additional resources and tutorials

### Community Resources
- **Tutorial Videos**: Step-by-step guides for common use cases
- **Example Projects**: Sample implementations and use cases
- **Best Practices**: Recommended approaches and patterns
- **FAQ**: Answers to frequently asked questions

---

## 🏆 Acknowledgments

### Open Source Contributors
Special thanks to the open source community for providing the foundational technologies that make Tripmate possible.

### Technology Partners
- **Portia AI**: For advanced AI orchestration capabilities
- **Google**: For powerful Gemini language models
- **Tavily**: For comprehensive search and discovery services

---

<div align="center">
  <p><strong>Made with ❤️ by the Yash Kumar</strong></p>
  <p>Transform your travel planning experience with the power of AI</p>
  
     [![GitHub stars](https://img.shields.io/github/stars/yashhkumarr/tripmate?style=social)](https://github.com/yashhkumarr/tripmate)
   [![GitHub forks](https://img.shields.io/github/forks/yashhkumarr/tripmate?style=social)](https://github.com/yashhkumarr/tripmate)
   [![GitHub issues](https://img.shields.io/github/issues/yashhkumarr/tripmate)](https://github.com/yashhkumarr/tripmate/issues)
   [![GitHub license](https://img.shields.io/github/license/yashhkumarr/tripmate)](https://github.com/yashhkumarr/tripmate/blob/main/LICENSE)
</div>
