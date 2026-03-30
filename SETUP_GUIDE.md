# GitHub Repository Setup Guide

## Overview
This guide explains how to set up a GitHub repository for the Photovoltaic Panel Parameter Monitor project.

## Step 1: Prepare Project Files
The project has been organized into a clean structure that excludes large binary files:
- Source code in `Code/` directory
- Documentation in `Documentation/` directory
- Build instructions and setup guides
- Git configuration files

## Step 2: Create GitHub Repository
1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right and select "New repository"
3. Configure repository:
   - **Repository name**: `pv-panel-monitor` or similar
   - **Description**: "STM32-based photovoltaic panel parameter monitoring system"
   - **Visibility**: Public (recommended for academic projects)
   - **Initialize with README**: Uncheck (we have our own)
   - **Add .gitignore**: Uncheck (we have our own)
   - **License**: Optional - choose MIT or similar

## Step 3: Upload Project to GitHub

### Option A: Using Command Line (Recommended)
```bash
# Navigate to project directory
cd path/to/Group8_Clean

# Initialize Git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Photovoltaic Panel Parameter Monitor Project"

# Add remote repository
git remote add origin https://github.com/your-username/repository-name.git

# Push to GitHub
git push -u origin main
```

### Option B: Using GitHub Desktop
1. Open GitHub Desktop
2. Select "File" → "Add Local Repository"
3. Browse to the `Group8_Clean` folder
4. Click "Create Repository"
5. Write commit message and click "Commit to main"
6. Click "Publish repository" to upload to GitHub

### Option C: Using Scripts (Windows)
1. Double-click `INIT_GIT_REPO.bat`
2. Follow the instructions shown

### Option D: Using Python Script
```bash
python init_git_repo.py
```

## Step 4: Verify Repository
1. Visit your GitHub repository page
2. Verify all files are present:
   - README.md
   - Code/ directory with source files
   - Documentation/ directory
   - Build instructions
   - .gitignore file

## Step 5: Share Repository
1. Copy the repository URL
2. Share with team members and instructors
3. Consider adding collaborators in repository settings

## File Structure in Repository
```
pv-panel-monitor/
├── README.md                 # Main project documentation
├── .gitignore               # Git ignore rules
├── BUILD_INSTRUCTIONS.md    # Build and setup guide
├── SETUP_GUIDE.md           # This file
├── INIT_GIT_REPO.bat        # Windows setup script
├── init_git_repo.py         # Python setup script
├── Code/                    # Source code
│   └── Core/               # Application code
├── Documentation/           # Project documentation
│   └── PROJECT_SUMMARY.md  # Project overview
```

## Notes on Large Files
The repository excludes:
- Large PowerPoint presentations (.pptx)
- Video files (.mp4)
- Large PDF documents
- Binary build artifacts

These files can be:
1. Shared via cloud storage (Google Drive, OneDrive)
2. Uploaded to GitHub using Git LFS (Large File Storage)
3. Compressed or converted to smaller formats

## Troubleshooting

### Common Issues
1. **Authentication errors**: Use SSH keys or personal access tokens
2. **Large file warnings**: Ensure .gitignore excludes binary files
3. **Push rejected**: Pull latest changes first: `git pull origin main`
4. **File not found**: Check file paths and case sensitivity

### Getting Help
- GitHub Documentation: https://docs.github.com
- Git Documentation: https://git-scm.com/doc
- Stack Overflow for specific error messages

## Next Steps
1. Set up continuous integration (optional)
2. Add issue templates for bug reports
3. Create wiki pages for detailed documentation
4. Set up project boards for task management